# This is a basic script for Syncing the entire Android Open Source Project for building.
import os
import sys
print ("============================================================")
print ("      Welcome to LineageOS Sync Script    ")
print ("============================================================")
n=input("Press Y/y to Continue, N/n to Exit: ")
if (n=="Y") or (n=="y") :
    print("Starting Sync")
    print("Warning: Repo is needed to be installed in prior of running this script")
    branch = input("Enter the branch name to sync: ")
    os.system('repo init -u https://www.github/LineageOS/android.git -b {branch}')
    print ("Starting Repo Sync")
    os.system('repo sync -c --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j8')
else :
    print("Re run script to start sync incase you mistakenly pressed 'N' ")
    
