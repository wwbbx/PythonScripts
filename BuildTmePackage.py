import os
import subprocess

def GetVersion():
	f = open(r'C:\SVN\HubDataServices\Trunk\Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\TMEPlatformAgentSetup.vdproj')

	for line in f:
		if "ProductVersion" in line:
			version = line[line.index('"8:')+3:-2]
			return version

def BuildSetupPackage():
	devenv = r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE\devenv.exe'
	setupProject = r'C:\SVN\HubDataServices\Trunk\Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\TMEPlatformAgentSetup.vdproj'

	packageFile = r'C:\SVN\HubDataServices\Trunk\Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\Debug\TMEPlatformAgent.msi'
	if(os.path.isfile(packageFile)):
		subprocess.call("del {0}".format(packageFile), shell=True)

	command = "\"{0}\" \"{1}\" /build Debug".format(devenv, setupProject)
	print command
	subprocess.call(command, shell=True)

	if os.path.isfile(packageFile):
		print 'Successfully built {0}!'.format(packageFile)

def CopyPackage(version):
	source = r'C:\SVN\HubDataServices\Trunk\Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\Debug\TMEPlatformAgent.msi'
	destination = r'\\fas3000-b.chn.agilent.com\v6\WCSS_Eng_STE\TME_EXTRACTOR\SOFTWARES\TMEPlatformAgent_{0}.msi'.format(version)

	command = "copy /Y /V {0} {1}".format(source, destination)
	if os.path.isfile(source):
		subprocess.call(command, shell=True)
	else:
		print "TMEPlatformAgent.msi is not exist. Can't copy."

	if os.path.isfile(destination):
		print 'Successfully copied {0}!'.format(destination)

version = GetVersion()
BuildSetupPackage()
CopyPackage(version)
