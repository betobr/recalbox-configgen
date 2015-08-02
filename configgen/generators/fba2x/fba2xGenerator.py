#!/usr/bin/env python
import Command
import fba2xControllers
import recalboxFiles
import fba2xConfig
import shutil
from generators.Generator import Generator
import os.path


class Fba2xGenerator(Generator):
    # Main entry of the module
    # Configure fba and return a command
    def generate(self, system, rom, playersControllers):
        # Settings recalbox default config file if no user defined one
        if not system.config['configfile']:
            # Using recalbox config file
            system.config['configfile'] = recalboxFiles.fbaCustom
            # Copy original fba2x.cfg
            shutil.copyfile(recalboxFiles.fbaCustomOrigin, recalboxFiles.fbaCustom)
            #  Write controllers configuration files
            fba2xControllers.writeControllersConfig(system, rom, playersControllers)
            # Write configuration to retroarchcustom.cfg
            fba2xConfig.writeFBAConfig(system)

        # the command to run
        commandline = '{} --configfile "{}" "{}"'.format(recalboxFiles.fba2xBin, system.config['configfile'], rom)
        return Command.Command(videomode=system.config['videomode'], commandline=commandline)