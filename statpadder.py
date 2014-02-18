import os
import cPickle
import base64
import struct
import datetime
import math
import time
import sys
import json
from PyQt4 import QtCore, QtGui
from mainUi import Ui_MainWindow


class Main (QtGui.QMainWindow):

    def __init__(self):

        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.resetToggle.clicked.connect(self.resetSession)
        self.ui.settingsButton.clicked.connect(self.get_dossier_location)
        self.dossier_folder = None

        self.path = self.module_path()

        self.tankdata = self.get_json_data(os.path.join(self.path, 'data', 'tanks.json'))
        self.mapdata = self.get_json_data(os.path.join(self.path, 'data', 'maps.json'))
        stuctures = [10, 17, 18, 20, 22, 24, 26, 27, 28, 29, 65, 69]
        self.structdata = dict()
        self.tanks = []

        for sid in stuctures:
            structfile = os.path.join(self.path, 'data', 'structures_'+str(sid)+'.json')
            self.structdata[sid] = self.get_json_data(structfile)


        if os.path.exists('settings.cfg'):
            self.settings = self.get_json_data(os.path.join(self.path, 'settings.cfg'))
            if os.path.exists(self.settings['dossier_path']):
                self.dossier_folder = self.settings['dossier_path']
        else:
            dpath = os.path.join(os.environ['APPDATA'], "Wargaming.net", "WorldOfTanks", "dossier_cache")
            if not os.path.exists(dpath):
                dpath = None
            self.settings = {
                'update_interval': 10,
                'dossier_path': dpath
            }
        self.running=True
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainloop)
        self.timer.start(self.settings['update_interval']*1000)

        self.last = 0
        self.results = []
        self.sessionStart = []

    def we_are_frozen(self):
        """Returns whether we are frozen via py2exe.
        This will affect how we find out where we are located."""

        return hasattr(sys, "frozen")


    def module_path(self):
        """ This will get us the program's directory,
        even if we are frozen using py2exe"""

        if self.we_are_frozen():
            return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))

        return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

    def savesettings(self):
        settings = json.dumps(self.settings)
        fh = open(os.path.join(self.path, 'settings.cfg'), 'w')
        fh.write(settings)
        fh.close()

    def get_dossier_location(self):
        self.dossier_folder = str(QtGui.QFileDialog.getExistingDirectory(self, 'Dossier Location', self.settings['dossier_path']))
        self.settings['dossier_path'] = self.dossier_folder
        self.savesettings()
        self.mainloop()

    def get_latest (self):
        latest = ['',0]
        for subdir, dirs, files in os.walk(self.dossier_folder, False):
            for name in files:
                target = os.path.join(subdir, name)
                mod = os.path.getmtime(target)
                if mod > latest[1]:
                    latest[0] = target
                    latest[1] = mod

        return latest

    def resetSession(self):
        self.last = 0
        self.sessionStart = self.results
        self.drawstats()


    def drawstats (self):
        battleSession = winSession = wrSession = wrChange = ratingTotal = ratingSession = fragsAvg = fragsChange = dmgAvg = dmgChange = spotAvg = spotChange = defAvg = defChange = tierSession = tierChange = wn7change = 0.0

        diff = []
        norm = []
        for i, s in enumerate(zip(self.results, self.sessionStart)):

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
            dmgChange = norm[4]
            spotAvg = diff[3]/diff[0]
            spotChange = norm[3]
            defAvg = diff[6]/diff[0]
            defChange = norm[6]
            tierSession = diff[7]/diff[0]
            tierChange = norm[7]
            wn7change = diff[8]


        #[0:battles, 1:wins, 2:frags, 3:spot, 4:damage, 5:cap, 6:defn, 7:tierpoints, 8:wn7]
        self.ui.battleSession.setText('%.2f' % battleSession)
        self.ui.winSession.setText('%.2f' % winSession)
        self.ui.wrSession.setText('%.2f%%' % wrSession)
        self.ui.wrChange.setText('%.3f%%' % wrChange)
        self.ui.ratingTotal.setText('%.2f' % ratingTotal)
        self.ui.ratingSession.setText('%.2f' % ratingSession)
        self.ui.fragsAvg.setText('%.2f' % fragsAvg)
        self.ui.fragsChange.setText('%.3f' % fragsChange)
        self.ui.dmgAvg.setText('%.2f' % dmgAvg)
        self.ui.dmgChange.setText('%.4f' % dmgChange)
        self.ui.spotAvg.setText('%.2f' % spotAvg)
        self.ui.spotChange.setText('%.3f' % spotChange)
        self.ui.defAvg.setText('%.2f' % defAvg)
        self.ui.defChange.setText('%.3f' % defChange)
        self.ui.tierSession.setText('%.1f' % tierSession)
        self.ui.tierChange.setText('%.4f' % tierChange)
        self.ui.change.setText('%.4f' % wn7change)

        self.setColor(self.ui.dmgChange, dmgChange)
        self.setColor(self.ui.spotChange, spotChange)
        self.setColor(self.ui.defChange, defChange)
        self.setColor(self.ui.wrChange, wrChange)
        self.setColor(self.ui.tierChange, 0-tierChange)
        self.setColor(self.ui.fragsChange, fragsChange)
        self.setColor(self.ui.change, wn7change)



        wn7scale = [424.0, 794.0, 1174.0, 1569.0, 1884.0, 999999999.0]
        wn7colors = ["#FE0E00", "#FE0E00", "#FE7903", "#F8F400", "#60FF00", "#02C9B3", "#D042F3"]

        self.setColor(self.ui.ratingTotal, ratingTotal, levels=wn7scale, colors=wn7colors)
        self.setColor(self.ui.ratingSession, ratingSession, levels=wn7scale, colors=wn7colors)
        self.setColor(self.ui.wrSession, wrSession, levels=[46.0, 48.0, 51.0, 56.0, 63.0, 1000.0], colors=wn7colors)
        self.setColor(self.ui.tierSession, tierSession, levels=[2.0,5.0,7.0, 9.0, 100.0], colors=["#D042F3", "#D042F3", "#02C9B3", "#60FF00", "#F8F400", "#FE0E00"])




    def setColor(self, target, value, levels=[0.0, 999999999999.9], colors=['#FF0000', '#FF0000', '#00FF00'], stationary=0, stationary_color='#FFFFFF'):
        levels_sorted = sorted(levels)
        color = colors[0]

        if stationary == value:
            color = stationary_color
        else:
            for num, level in enumerate(levels_sorted):
                if value <= level:
                    color = colors[num+1]
                    break
        target.setStyleSheet('QLabel {color: '+color+'}')



    def mainloop(self):
        if self.dossier_folder:
            dossierfile = self.get_latest()
            if dossierfile[1] > self.last:
                self.tanks = []
                self.last = dossierfile[1]
                newresults = self.process_file(dossierfile[0])
                if not newresults == self.results:
                    if self.sessionStart == []:
                        self.sessionStart = newresults
                    self.results = newresults
                    self.drawstats()
                




    def process_file(self, filename):
        global tankdata, mapdata, structdata, tanks
        cachefile = open(filename, 'rb')
        dossierversion, dossierCache = cPickle.load(cachefile)


        
        tankitems = [(k, v) for k, v in dossierCache.items()]
        base32name = base64.b32decode(os.path.splitext(os.path.basename(filename))[0].replace('.\\', ''))
        
        dossier = dict()
            
        dossierheader = dict()
        dossierheader['dossierversion'] = str(dossierversion)
        dossierheader['parser'] = 'statpadder'
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


            if tank['version'] < 65:

                for k in self.structdata[tank['version']]:
                    if k['category'] == "tankdata":
                        tank[k['name']] = self.get_data(sourcedata, k['offset'], k['length'])

            if tank['version'] >= 65:
                if tank['version'] == 65:
                    blocks = ('a15x15', 'a15x15_2', 'clan', 'clan2', 'company', 'company2', 'a7x7', 'achievements', 'frags', 'total', 'max15x15', 'max7x7')
                if tank['version'] == 69:
                    blocks = ('a15x15', 'a15x15_2', 'clan', 'clan2', 'company', 'company2', 'a7x7', 'achievements', 'frags', 'total', 'max15x15', 'max7x7', 'playerInscriptions', 'playerEmblems', 'camouflages', 'compensation', 'achievements7x7')
                blockcount = len(list(blocks))+1
                newbaseoffset = (blockcount * 2)
                header = struct.unpack_from('<' + 'H' * blockcount, data)
                blocksizes = list(header[1:])
                blocknumber = 0
                fragslist = []
                numoffrags_list = 0
                numoffrags_a15x15 = 0
                
                for blockname in blocks:
                    if blocksizes[blocknumber] > 0:
                        if blockname == 'frags':
                                fmt = '<' + 'IH' * (blocksizes[blocknumber]/6)
                                fragsdata = struct.unpack_from(fmt, data, newbaseoffset)
                                
                                for x in range(0, blocksizes[blocknumber]):
                                    dossier[newbaseoffset+x] = str(sourcedata[newbaseoffset+x]) + " / Frags; "

                                index = 0
                                for i in xrange((blocksizes[blocknumber]/6)):
                                    compDescr, amount = (fragsdata[index], fragsdata[index + 1])
                                    numoffrags_list += amount   
                                    frag_countryid, frag_tankid, frag_tanktitle = self.get_tank_details(compDescr, self.tankdata)
                                    tankfrag = [frag_countryid, frag_tankid, amount, frag_tanktitle]
                                    fragslist.append(tankfrag)
                                    index += 2
                            
                                newbaseoffset += blocksizes[blocknumber]
                            
                        else:
                            oldbaseoffset = newbaseoffset
                            structureddata = self.get_structured_data(sourcedata, data, dossier, blockname, tank['version'], newbaseoffset)
                            newbaseoffset = oldbaseoffset+blocksizes[blocknumber]
                            tank[blockname] = structureddata

                    blocknumber +=1

            self.get_interesting_data(tank)

            self.tanks.append(tank)

        battles = wins = frags = spot = damage = cap = defn = tierpoints = 0

        for tank in self.tanks:
            if 'battlesCount' in tank:
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

    def get_interesting_data(self, tank):
        keys = ('a15x15', 'a15x15_2') # 'clan', 'clan2', 'company', 'company2'
        useful_data = {'battlesCount', 'wins', 'frags', 'spotted','damageDealt', 'capturePoints', 'droppedCapturePoints'}

        for item in keys:
            if item in tank:
                for useful_key in useful_data:
                    if useful_key in tank[item]:
                        if not useful_key in tank:
                            tank[useful_key] = tank[item][useful_key]
                        else:
                            tank[useful_key] += tank[item][useful_key]
        return tank

    def get_json_data(self, filename):
        if not os.path.exists(filename) or not os.path.isfile(filename) or not os.access(filename, os.R_OK):
            raise NameError('CANNOT FIND FILE: '+str(filename))
            sys.exit(1)
        file_json = open(filename, 'r')
        try:
            file_data = json.load(file_json)
        except Exception, e:
            sys.exit(1)
        file_json.close()
        return file_data

    def get_tank_data(self, countryid, tankid, dataname):
        for tankdata in self.tankdata:
            if tankdata['countryid'] == countryid:
                if tankdata['tankid'] == tankid:
                    return tankdata[dataname]

        return "-"

    def get_tank_details(self, compDescr, tanksdata):

        tankid = compDescr >> 8 & 65535
        countryid = compDescr >> 4 & 15
            
        tankname = self.get_tank_data(countryid, tankid, "title")

        return countryid, tankid, tankname

    def get_structured_data(self, sourcedata, data, rawdata, category, tankversion, baseoffset):
        returndata = dict()

        for structureitem in self.structdata[tankversion]:
            if category == structureitem['category']:
                if tankversion == structureitem['version']:
                    offset = structureitem['offset']
                    if baseoffset > 0:
                        offset += baseoffset
                    returndata[structureitem['name']] = self.get_new_data(sourcedata, data, rawdata, category + " " + structureitem['name'], offset, structureitem['length'])

        return returndata

    def get_data(self, sourcedata, offset, length):
        value = sourcedata[offset]
        for i in range(1,length):
            value = value + pow(256, i)*sourcedata[offset+i]
        return value

    def get_new_data(self, sourcedata, data, dossier, name, startoffset, offsetlength):
        
        if len(data)<startoffset+offsetlength:
            return 0
        
        structformat = 'H'

        if offsetlength==1:
            structformat = 'B'

        if offsetlength==2:
            structformat = 'H'
            
        if offsetlength==4:
            structformat = 'I'


        value = struct.unpack_from('<' + structformat, data, startoffset)[0]
        
        for x in range(0, offsetlength):
            dossier[startoffset+x] = str(sourcedata[startoffset+x]) + " / " + str(value) +  "; " + name

        
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