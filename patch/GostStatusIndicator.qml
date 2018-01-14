import QtQuick 2.0
import Sailfish.Silica 1.0
import org.nemomobile.systemsettings 1.0
import Nemo.DBus 2.0

Item {
    id: gostStatusIndicator
    property bool updatesEnabled: true
    property bool activeState: false

    width: icon.width
    height: icon.height
    visible: icon.status == Image.Ready

    Image {
        id: icon
        source: "image://theme/icon-status-gost-button"
        opacity: activeState ? 1 : 0
        Behavior on opacity { FadeAnimation { } }
    }
    
    DBusInterface {
        id: proxyBus
        bus: DBus.SystemBus
        service: "xyz.birdzhang.gost.global"
        path: "/xyz/birdzhang/gost/global"
        iface: "xyz.birdzhang.gost.global"

        signalsEnabled: true
        function statusChanged(status){
            console.log("status changed", status)
           if(status && status == "start"){
              activeState = true;
           }else{
              activeState = false;
           }
        }
        
    }
    
}