import os
import cPickle
import base64
import struct
import datetime
import math
import time
import sys
from PyQt4 import QtCore, QtGui
from mainUi import Ui_MainWindow

dossier_folder = "C:\Users\Nic West\AppData\Roaming\Wargaming.net\WorldOfTanks\dossier_cache"

class Main (QtGui.QMainWindow):

    def __init__(self):

        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tankdata = self.get_json_data('data/tanks.json')
        self.mapdata = self.get_json_data('data/maps.json')
        stuctures = [18, 20, 22, 24, 26, 27, 28, 29]
        self.structdata = dict()
        self.tanks = []

        for sid in stuctures:
            structfile = os.path.join('data', 'structures_'+str(sid)+'.json')
            self.structdata[sid] = self.get_json_data(structfile)

        self.running=True
        
        self.timer =  QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainloop)
        self.timer.start(10000)

        self.last = 0
        self.results = []
        self.sessionStart = []

    def get_latest (self):
        latest = ['',0]
        for subdir, dirs, files in os.walk(dossier_folder, False):
            for name in files:
                target = os.path.join(subdir, name)
                mod = os.path.getmtime(target)
                if mod > latest[1]:
                    latest[0] = target
                    latest[1] = mod

        return latest



    def mainloop (self):
        print "yayay!"
        dossierfile = self.get_latest()
        if dossierfile[1] > self.last:
            self.tanks = []
            self.last = dossierfile[1]
            newresults = self.process_file(dossierfile[0])
            if not newresults == self.results:
                if self.sessionStart == []:
                    self.sessionStart = newresults
                self.results = newresults

                battleSession = winSession = wrSession = wrChange = ratingTotal = ratingSession = fragsAvg = fragsChange = dmgAvg = dmgChange = spotAvg = spotChange = defAvg = defChange = tierSession = tierChange = 0.0

                diff = []
                norm = []
                import random
                for s in zip(self.results, self.sessionStart):
                    # s = (s[0]+random.uniform(10,90), s[1])
                    diff.append(float(s[0]-s[1]))
                    if s[0]-s[1] > 0:
                        norm.append((float(s[0])/float(self.results[0]))-(float(s[1])/float(self.sessionStart[0])))
                    else:
                        norm.append(0.0)

                print diff

                ratingTotal = self.results[8]
                ratingSession = self.calc_wn7(diff[0], diff[1], diff[2], diff[3], diff[4], diff[5], diff[6], diff[7])
                if diff[0] > 0:
                    battleSession = diff[0]
                    winSession = diff[1]
                    wrSession = (diff[1]/diff[0])*100
                    wrChange = norm[1]*100
                    fragsAvg = diff[2]/diff[0]
                    fragsChange = norm[2]
                    dmgAvg = diff[4]/diff[0]
                    dmgChange = norm[2]
                    spotAvg = diff[3]/diff[0]
                    spotChange = norm[3]
                    defAvg = diff[6]/diff[0]
                    defChange = norm[6]
                    tierSession = diff[7]/diff[0]
                    tierChange = norm[7]


                #[0:battles, 1:wins, 2:frags, 3:spot, 4:damage, 5:cap, 6:defn, 7:tierpoints, 8:wn7]
                self.ui.battleSession.setText('%.2f' % battleSession)
                self.ui.winSession.setText('%.2f' % winSession)
                self.ui.wrSession.setText('%.2f%%' % wrSession)
                self.ui.wrChange.setText('%.2f%%' % wrChange)
                self.ui.ratingTotal.setText('%.2f' % ratingTotal)
                self.ui.ratingSession.setText('%.2f' % ratingSession)
                self.ui.fragsAvg.setText('%.2f' % fragsAvg)
                self.ui.fragsChange.setText('%.2f' % fragsChange)
                self.ui.dmgAvg.setText('%.2f' % dmgAvg)
                self.ui.dmgChange.setText('%.2f' % dmgChange)
                self.ui.spotAvg.setText('%.2f' % spotAvg)
                self.ui.spotChange.setText('%.2f' % spotChange)
                self.ui.defAvg.setText('%.2f' % defAvg)
                self.ui.defChange.setText('%.2f' % defChange)
                self.ui.tierSession.setText('%.2f' % tierSession)
                self.ui.tierChange.setText('%.2f' % tierChange)




    def process_file(self, filename):
        global tankdata, mapdata, structdata, tanks
        cachefile = open(filename, 'rb')
        cacheobject = cPickle.load(cachefile)
        dossierCache = cacheobject[1]

        
        tankitems = [(k, v) for k, v in dossierCache.items()]
        base32name = base64.b32decode(os.path.splitext(os.path.basename(filename))[0].replace('.\\', ''))
        
        dossier = dict()
            
        dossierheader = dict()
        dossierheader['dossierversion'] = str(cacheobject[0])
        dossierheader['parser'] = 'http://www.vbaddict.net/wot'
        dossierheader['tankcount'] = len(tankitems)

        
        dossierheader['server'] = base32name.split(';', 1)[0];
        dossierheader['username'] = base32name.split(';', 1)[1];

        for tankitem in tankitems:
            tank = dict()
            tank['tankid'] = tankitem[0][1] >> 8 & 65535
            tank['countryid'] = tankitem[0][1] >> 4 & 15
            data = tankitem[1][1]
            tankstruct = str(len(data)) + 'B'
            sourcedata = struct.unpack(tankstruct, data)
            tank['version'] = sourcedata[0]
            tank['name'] = self.get_tank_data(tank['countryid'], tank['tankid'], 'title')
            tank['tier'] = self.get_tank_data(tank['countryid'], tank['tankid'], 'tier')

            for k in self.structdata[tank['version']]:
                if k['category'] == "tankdata":
                    tank[k['name']] = self.get_data(sourcedata, k['offset'], k['length'])
            self.tanks.append(tank)

        battles = wins = frags = spot = damage = cap = defn = tierpoints = 0

        for tank in self.tanks:
            battles = battles + int(tank['battlesCount'])
            wins = wins + int(tank['wins'])
            frags = frags + int(tank['frags'])
            spot = spot + int(tank['spotted'])
            damage = damage + int(tank['damageDealt'])
            cap = cap + int(tank['capturePoints'])
            defn = defn + int(tank['droppedCapturePoints'])
            tierpoints = tierpoints + (int(tank['tier'])*int(tank['battlesCount']))

        wn7 = self.calc_wn7(battles, wins, frags, spot, damage, cap, defn, tierpoints)
        return [battles, wins, frags, spot, damage, cap, defn, tierpoints, wn7]

    def get_json_data(self, filename):
        import json, time, sys, os
        os.chdir(sys.path[0])
        if not os.path.exists(filename) or not os.path.isfile(filename) or not os.access(filename, os.R_OK):
            catch_fatal(filename + " does not exists!")
            sys.exit(1)
        file_json = open(filename, 'r')
        try:
            file_data = json.load(file_json)
        except Exception, e:
            catch_fatal(filename + " cannot be loaded as JSON: " + e.message)
            sys.exit(1)
        file_json.close()
        return file_data

    def get_tank_data(self, countryid, tankid, dataname):
        for tankdata in self.tankdata:
            if tankdata['countryid'] == countryid:
                if tankdata['tankid'] == tankid:
                    return tankdata[dataname]

        return "-"

    def get_data(self, sourcedata, offset, length):
        value = sourcedata[offset]
        for i in range(1,length):
            value = value + pow(256, i)*sourcedata[offset+i]
        return value

    def calc_wn7(self, battles, wins, frags, spot, damage, cap, defn, tierpoints):

        wn7 = 0.0

        if battles > 0:
            wr = float(wins)/float(battles) *100
            tier = float(tierpoints)/float(battles)
            dmg = float(damage)/float(battles)
            sp = float(spot)/float(battles)
            frg = float(frags)/float(battles)
            df = float(defn)/float(battles)

            wn7 = (1240.0-(1040.0/pow(min(tier,6),0.164)))*frg
            wn7 = wn7 + (dmg*530)/(184*pow(math.e, 0.24*tier) +130)
            wn7 = wn7 + sp*125*min(tier, 3)/3
            wn7 = wn7 + min(df,2.2)*100
            wn7 = wn7 + ((185.0/(0.17+ pow(math.e, (wr-35)*-0.134)))-500)*0.45
            wn7 = wn7 - ((5 - min(tier,5))*125) / (1 + pow(math.e, (tier - pow((battles/220), 3/tier))) *1.5 )


        return wn7

def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    window.mainloop()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()