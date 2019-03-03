#!/bin/sh
    echo "Content-type: text/html\n"
     
    # read in our parameters
    CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
    FOLDER=`echo "$QUERY_STRING" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
     FOLDER1=`echo "$QUERY_STRING" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
FOLDER2=`echo "$QUERY_STRING" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

    # our html header
    echo "<html>"
    echo "<head><title>Bash CGI</title></head>"
    echo "<body>"
     
    # test if any parameters were passed
    if [ $CMD ]
    then
      case "$CMD" in
        ip)
          echo "Output of ip a :<pre>"
          /bin/ip a
          echo "</pre>"
          ;;
        adbdevices)
          echo "Output of adb devices :<pre>"
          /usr/bin/adb devices
          echo "</pre>"
          ;;
        adbhome)
          echo "Home button pressed :<pre>"
          /usr/bin/adb shell input keyevent 3
          echo "</pre>"
          ;;
        adbmenu)
          echo "Menu button pressed:<pre>"
          /usr/bin/adb shell input keyevent 1
          echo "</pre>"
          ;; 
        adbback)
          echo "Back button pressed:<pre>"
          /usr/bin/adb shell input keyevent 4
          echo "</pre>"
          ;;
        adbvolumeup)
          echo "Volume Up :<pre>"
          /usr/bin/adb shell input keyevent 24
          echo "</pre>"
          ;;
        adbvolumedown)
          echo "Volume Down :<pre>"
          /usr/bin/adb shell input keyevent 25
          echo "</pre>"
          ;;
        adbup)
          echo "Up button pressed:<pre>"
          /usr/bin/adb shell input keyevent 19
          echo "</pre>"
          ;;


        adbdown)
          echo "Down button pressed :<pre>"
          /usr/bin/adb shell input keyevent 20
          echo "</pre>"
          ;;

        adbleft)
              echo "Left button pressed :<pre>"
              /usr/bin/adb shell input keyevent 21
              echo "</pre>"
              ;;
        adbright)
              echo "Right button pressed :<pre>"
              /usr/bin/adb shell input keyevent 22
              echo "</pre>"
              ;;


        adbinput)
          echo "Output of adb shell input text $FOLDER :<pre>"
          /usr/bin/adb shell input text "$FOLDER"
          echo "</pre>"
          ;;
     
            adbconnect)
              echo "Output of  adb connect $FOLDER1 :<pre>"
              /usr/bin/adb connect "$FOLDER1"
              echo "</pre>"
              ;;
            *)
          echo "Unknown command $CMD<br>"
          ;;
      esac
    fi
     
    # print out the form
     
    # page header
    echo "<p>"
    echo "<center>"
    echo "<h2>Glass Control</h2>"
    echo "</center>"
    echo "<p>"
    echo "<p>"
     
    echo "Choose which command you want to run"
    echo "<form method=get>"
    echo "<input type=radio name=cmd value=ip checked>ip a  <br>"
    echo "<input type=radio name=cmd value=adbdevices> adb devices<br>"
    echo "<input type=radio name=cmd value=adbhome> Home button <br>"
    echo "<input type=radio name=cmd value=adbmenu> Menu button <br>"
    echo "<input type=radio name=cmd value=adbback> Back button  <br>"
    echo "<input type=radio name=cmd value=adbvolumeup> Volume Up <br>"
    echo "<input type=radio name=cmd value=adbvolumedown> Volume Down <br>"
    echo "<input type=radio name=cmd value=adbup> Up button <br>"
    echo "<input type=radio name=cmd value=adbdown> Down button <br>"
    echo "<input type=radio name=cmd value=adbleft> Left button <br>"
    echo "<input type=radio name=cmd value=adbright> Right button <br>"
    echo "<input type=radio name=cmd value=adbinput> adb shell input text <input type=text name=folder value=text><br>"
    echo "<input type=radio name=cmd value=adbconnect>  adb connect <input type=text name=folder1 value=192.168.1.237:5555><br>"
    echo "<input type=submit>"
    echo "</form>"
    echo "</body>"
    echo "</html>"
