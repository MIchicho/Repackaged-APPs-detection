#!/usr/bin/env python
# coding=utf-8
# Author   :   Chicho
# Date     :   2017-05-12
# Running  :   python deleteAds.py
# function :   delete the ad libraries

import os

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"

orioutPutPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original/"

repoutPutPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged/"

def deleteAds(Path,outputPath):

    apkList = os.listdir(Path)

    for apk in apkList:

        apkPath = os.path.join(Path,apk)
        
        apkoutPutPath = os.path.join(outputPath,apk)

        f = open(apkPath)

        lineList = f.readlines()

        count = 0

        for line in lineList:

            if line.startswith("Lcom/umeng/"):
                continue

            if line.startswith("Lcom/games/"):
                continue

            if line.startswith("Lcom/google/ads/"):
                continue 

            if line.startswith("Lcom/google/analytics/"):
                continue

            if line.startswith("Lcom/google/gson"):
                continue

            if line.startswith("Ltwitter4j/"):
                continue

            if line.startswith("Lcom/millennialmedia/"):
                continue


            if line.startswith("Lcom/scoreloop/client/"):
                continue

            if line.startswith("Lcom/unity3d/ads"):
                continue

            if line.startswith("Lcom/flurry/"):
                continue

            if line.startswith("Lorg/apache/harmony/javax"):
                continue

            if line.startswith("Lcom/google/common/"):
                continue

            if line.startswith("Lcom/applovin/"):
                continue

            if line.startswith("Lcom/inmobi/"):
                continue

            if line.startswith("Lcom/heyzap/sdk/ads"):
                continue

            if line.startswith("Lorg/json/heyzap/"):
                continue

            if line.startswith("Lcn/domob/"):
                continue

            if line.startswith("Lcom/mobclix"):
                continue

            if line.startswith("Lcom/suizong/mobile/ads/"):
                continue

            if line.startswith("Lcom/comscore/"):
                continue

            if line.startswith("Lcom/admob/android/ads"):
                continue
            
            if line.startswith("Lcom/adknowledge/superrewards/"):
                continue

            if line.startswith("Lcom/crossfield/"):
                continue

            if line.startswith("Lmediba/ad/sdk/android"):
                continue

            if line.startswith("Lcom/admarvel/"):
                continue

            if line.startswith("Lcom/jirbo/"):
                continue

            if line.startswith("Lcom/playhaven/"):
                continue

            if line.startswith("Lorg/anddev/andengine"):
                continue

            if line.startswith("Lcom/tapjoy"):
                continue

            if line.startswith("Lcom/amoad"):
                continue

            if line.startswith("Lcom/bodong/"):
                continue

            if line.startswith("Lcom/mopub"):
                continue

            if line.startswith("Lcom/yume"):
                continue
            
            if line.startswith("Lcom/adwhirl"):
                continue

            if line.startswith("Lcom/digitalsunray/advantage"):
                continue

            if line.startswith("Lcom/crformeout/admob"):
                continue

            if line.startswith("Lcom/mobclix/android"):
                continue

            if line.startswith("Lcom/spice/ads"):
                continue

            if line.startswith("Lcom/smartadserver/library"):
                continue

            if line.startswith("Lcom/aquafadas/"):
                continue

            if line.startswith("Lcom/citygrid/ads"):
                continue

            if line.startswith("Lcom/dianjoy"):
                continue

            if line.startswith("Lcom/scoopma/ads"):
                continue

            if line.startswith("Lcom/rhythmnewmedia/android"):
                continue

            if line.startswith("Lcom/zestadz/android"):
                continue

            if line.startswith("Lcom/papaya/"):
                continue

            if line.startswith("Lcom/vungle/sdk"):
                continue

            if line.startswith("Lcom/dianru/adsdk"):
                continue

            if line.startswith("Lcmm/ani/ad"):
                continue

            if line.startswith("Lcom/vpon/ads"):
                continue

            if line.startswith("Lcom/sessionm"):
                continue

            if line.startswith("Lcom/pocketchange/android"):
                continue

            if line.startswith("Lcom/dialogads"):
                continue

            if line.startswith("Lcom/kuad"):
                continue

            if line.startswith("Lcom/handyapps/houseads"):
                continue

            if line.startswith("Lcom/comscore"):
                continue

            if line.startswith("Lnet/cavas/show"):
                continue

            if line.startswith("Lcom/neodata/adagiosdk"):
                continue

            if line.startswith("Lcom/applift/playads"):
                continue

            if line.startswith("Lcom/motilityads"):
                continue

            if line.startswith("Lcom/geosophic"):
                continue

            if line.startswith("Lcom/tiger/adm"):
                continue

            if line.startswith("Lcom/gramble/sdk"):
                continue

            if line.startswith("Lcom/qwapi/adclient"):
                continue

            if line.startswith("Ladticker/library"):
                continue

            if line.startswith("Lcom/amobee/adsdk/"):
                continue

            if line.startswith("Lcom/adfonic/android"):
                continue

            if line.startswith("Lcom/admarvel"):
                continue

            if line.startswith("Lcom/onelouder/adlib"):
                continue

            if line.startswith("Lcom/adpooh"):
                continue

            if line.startswith("Lcom/otomod/ad"):
                continue

            if line.startswith("Lcom/madnet"):
                continue

            if line.startswith("Lcom/wisesharksoftware/ad"):
                continue

            if line.startswith("Lcom/appbucks"):
                continue

            if line.startswith("Lcom/senddroid"):
                continue

            if line.startswith("Lnet/adcrops/sdk"):
                continue

            if line.startswith("Lcom/jnj/mocospace"):
                continue

            if line.startswith("Lcom/anzhi/ad"):
                continue

            if line.startswith("Lcom/mraid"):
                continue

            if line.startswith("Lcom/lifestreet/android"):
                continue

            if line.startswith("Lcom/vdopia"):
                continue

            if line.startswith("Ljp/adresult"):
                continue

            if line.startswith("Lcom/mining/app"):
                continue

            if line.startswith("Lcom/adsdk/sdk"):
                continue

            if line.startswith("Lcom/rekmob/ads"):
                continue

            if line.startswith("Lanywheresoftware/b4a/admobwrapper"):
                continue

            if line.startswith("Lcom/incross/bkadlibrary"):
                continue

            if line.startswith("Lde/selfadservice"):
                continue

            if line.startswith("Lcom/adwo/adsdk"):
                continue

            if line.startswith("Lcom/adlocus"):
                continue

            if line.startswith("Lcom/airpush"):
                continue

            if line.startswith("Lcom/appbulous/adsdk"):
                continue

            if line.startswith("Lcom/nvnewvinny/adstatistics"):
                continue

            if line.startswith("Lroukiru/RLib/RAd"):
                continue

            if line.startswith("Lseventynine/sdk"):
                continue

            if line.startswith("Lio/presage/ads"):
                continue

            if line.startswith("Lcom/admogo"):
                continue

            if line.startswith("Lvnits/admob"):
                continue

            if line.startswith("Lcom/trymph/ads"):
                continue

            if line.startswith("Lcom/adtech/mobilesdk"):
                continue

            if line.startswith("Lcom/adview"):
                continue

            if line.startswith("Lcom/google/adgoji"):
                continue

            if line.startswith("Lcom/kiwi/ads"):
                continue

            if line.startswith("Lcom/gi/adslibrary"):
                continue

            if line.startswith("Lcom/appon/ads"):
                continue

            if line.startswith("Lcom/trialpay/android"):
                continue

            if line.startswith("Lcom/kauf"):
                continue

            # 83
            if line.startswith("Lcom/mobileroadie"):
                continue

            if line.startswith("Lcom/go"):
                continue

            if line.startswith("Lcom/nabrozidhs/admob"):
                continue

            if line.startswith("Lcom/pontilex"):
                continue

            if line.startswith("Lcom/gk/GKAd"):
                continue

            if line.startswith("Lus/jsy/ads"):
                continue

            if line.startswith("Lcom/admofi/sdk"):
                continue

            if line.startswith("Lcom/liquidm"):
                continue

            if line.startswith("Lcom/custom/ads"):
                continue

            if line.startswith("Lcom/tappx/ads"):
                continue

            if line.startswith("Lcom/cooguo/advideo"):
                continue

            if line.startswith("Lim/yixin/sdk"):
                continue

            if line.startswith("Lcom/adsage/sdk"):
                continue

            if line.startswith("Lcom/uucun/adsdk"):
                continue 
            #96
            if line.startswith("Lcom/adsdk"):
                continue

            if line.startswith("Lcom/slacker"):
                continue

            if line.startswith("Lcom/inneractive/api"):
                continue

            if line.startswith("Lcom/MadsAdview"):
                continue

            if line.startswith("Lru/adcamp/ads"):
                continue

            if line.startswith("Lcom/misterbell/advertising"):
                continue

            if line.startswith("Lcom/rebtel"):
                continue

            if line.startswith("Lcom/amaze/ad"):
                continue

            if line.startswith("Lcom/yoc"):
                continue

            if line.startswith("Lcom/ihs"):
                continue

            if line.startswith("Lcom/wandoujia/ads"):
                continue

            if line.startswith("Lru/aduwant/ads"):
                continue

            if line.startswith("Lcom/smaato/soma"):
                continue

            if line.startswith("Lsg/radioactive"):
                continue

            if line.startswith("Lcom/moonglabs/ads"):
                continue

            if line.startswith("Lcom/ru/weborama"):
                continue

            if line.startswith("Ltw/mobiforce"):
                continue

            if line.startswith("Lcom/am/adlib"):
                continue

            if line.startswith("Lcom/revmob"):
                continue

            if line.startswith("Lcom/zoonapp/adlib"):
                continue

            if line.startswith("Lcom/sd/ads"):
                continue

            if line.startswith("Lcom/gfan/sdk"):
                continue

            if line.startswith("Lcom/kiwiup/promotion"):
                continue

            if line.startswith("Lcom/adiquity/android"):
                continue

            if line.startswith("Lcn/appmedia/ad"):
                continue

            if line.startswith("Lcom/clickforce/ad"):
                continue

            if line.startswith("Lcom/ad_stir"):
                continue

            if line.startswith("Lcom/abc/testadmob"):
                continue

            if line.startswith("Lcom/mtrip"):
                continue

            if line.startswith("Lcom/hammerhead"):
                continue

            if line.startswith("Lcom/bfio/ad"):
                continue

            if line.startswith("Lcom/revolabinc/goodad"):
                continue

            if line.startswith("Lcom/util/adlib"):
                continue
            # 136
            if line.startswith("Lcom/turner/android"):
                continue
            
            if line.startswith("Llsh/ad"):
                continue

            if line.startswith("Lcom/qiang/escore"):
                continue

            if line.startswith("Lcom/purplebrain/adbuddiz"):
                continue

            if line.startswith("Lcn/waps/extend"):
                continue

            if line.startswith("Lin/spicelabs/ads"):
                continue

            if line.startswith("Lcom/adsmogo"):
                continue

            if line.startswith("Lcom/mobmatrix"):
                continue

            if line.startswith("Lcom/emar/escore"):
                continue

            if line.startswith("Lcom/pureagency/pureroi"):
                continue

            if line.startswith("Lnet/ldmobile/adit"):
                continue

            if line.startswith("Lcom/idc/advertisementlibrary"):
                continue

            if line.startswith("Lcom/tss21/ad"):
                continue

            if line.startswith("Lcom/adlooper/sdk"):
                continue

            if line.startswith("Lcom/full/fullad"):
                continue

            if line.startswith("Lcom/mobage"):
                continue

            if line.startswith("Lcom/playerize/supperwards"):
                continue

            if line.startswith("Lcom/appsfire/appbooster"):
                continue

            if line.startswith("Lcom/unity3d/ads"):
                continue

            if line.startswith("Ljp/gmotech/smaad"):
                continue

            if line.startswith("Lcom/adchina/android"):
                continue

            if line.startswith("Lcom/octobird/advertising"):
                continue

            if line.startswith("Lcom/ngigroup/adstir"):
                continue

            if line.startswith("Ljp/focas/adroute"):
                continue

            if line.startswith("Lcom/distilledmedia"):
                continue

            if line.startswith("Lcom/hyprmx/android"):
                continue

            if line.startswith("Ltv/freewheel/ad"):
                continue

            if line.startswith("Lcom/pinsightmediaplus/advertising"):
                continue

            if line.startswith("Lcom/hodo"):
                continue

            if line.startswith("Lcom/microeyes/admob"):
                continue

            if line.startswith("Ljp/adlantis"):
                continue

            if line.startswith("Lcom/voxel"):
                continue

            if line.startswith("Lcom/mini/loader"):
                continue

            if line.startswith("Lcom/massiveimpact"):
                continue

            if line.startswith("Lcom/widespace"):
                continue

            if line.startswith("Lcom/bravo/ads"):
                continue

            if line.startswith("Lvpoint/ads/obj"):
                continue

            if line.startswith("Lcom/adswizz/phantom"):
                continue

            if line.startswith("Lcom/appma/ad"):
                continue

            if line.startswith("Lcom/tokenads/sdk"):
                continue

            if line.startswith("Lcom/lmmob/ad"):
                continue

            if line.startswith("Lcom/igaworks/AdPOPcornTracerSDK"):
                continue

            if line.startswith("Lcom/vervewireless/advert"):
                continue

            if line.startswith("Lcom/jumptap/adtag"):
                continue

            if line.startswith("Lcom/tapifier/admob"):
                continue

            if line.startswith("Lcom/ad2play"):
                continue

            if line.startswith("Lcom/acerolamob"):
                continue

            if line.startswith("Lcom/webtrends/mobile"):
                continue

            if line.startswith("Lcom/mobcent/ad"):
                continue

            if line.startswith("Lcom/hiiir"):
                continue

            if line.startswith("Lnet/miidi/ad"):
                continue

            if line.startswith("Lcn/domob"):
                continue

            if line.startswith("Lorg/burlock/amazonads"):
                continue

            if line.startswith("Lcom/applifier/impact"):
                continue

            if line.startswith("Lcom/vpadn"):
                continue

            if line.startswith("Lcom/mobisage"):
                continue

            if line.startswith("Lcom/adappter/sdk"):
                continue

            if line.startswith("Lmobpartner/ad/sdk"):
                continue

            if line.startswith("Lcom/pennwell"):
                continue

            if line.startswith("Lcom/kuadcpa"):
                continue

            if line.startswith("Lcom/kpt/adaptxt"):
                continue

            if line.startswith("Lcom/tapit"):
                continue

            if line.startswith("Lcom/startapp/adnroid"):
                continue

            if line.startswith("Lcom/Leadbolt"):
                continue

            if line.startswith("Lcom/cyberbounty/adapplib"):
                continue

            if line.startswith("Liec/adcrosssell"):
                continue
            # 207
            if line.startswith("Lcom/adgoji"):
                continue

            if line.startswith("Lcom/sample/admob"):
                continue

            if line.startswith("Lcom/bitforce/apponsor"):
                continue

            if line.startswith("Lcom/rcplatform/ad"):
                continue

            if line.startswith("Ljason/advert/airpush"):
                continue

            if line.startswith("Lcom/gigigo/smartadserver2"):
                continue

            if line.startswith("Lcom/vodafone/amobee"):
                continue

            if line.startswith("Lcom/auditude/ads"):
                continue

            if line.startswith("Lcom/hotmob/android"):
                continue

            if line.startswith("Lcom/tomorrownetworks"):
                continue

            if line.startswith("Lcom/quantcast"):
                continue

            if line.startswith("Lcom/ad4kids/mobileads"):
                continue

            if line.startswith("Lcom/nexage/ormma"):
                continue

            if line.startswith("Lcom/ad4screen/sdk"):
                continue

            if line.startswith("Lcom/waystorm/ads"):
                continue

            if line.startswith("Lvn/adflex"):
                continue

            if line.startswith("Ljp/adstore/tracking"):
                continue

            if line.startswith("Lcom/adaffix/util"):
                continue

            if line.startswith("Lcom/appia"):
                continue

            if line.startswith("Lcom/fusepowered/ads"):
                continue

            if line.startswith("Lcom/waps/ads"):
                continue

            if line.startswith("Lcom/video/adsdk"):
                continue

            if line.startswith("Lcom/admore/mobile"):
                continue

            if line.startswith("Lcom/widdit"):
                continue

            if line.startswith("Lcom/mof/ad"):
                continue

            if line.startswith("Lcom/adfeiwo/ad"):
                continue

            if line.startswith("Lcom/mj/ad"):
                continue

            if line.startswith("Lcom/meidalets"):
                continue

            if line.startswith("Lcom/adpick/advertiser"):
                continue

            if line.startswith("Lcom/kuguo"):
                continue

            if line.startswith("Lcom/anttek/ad"):
                continue

            if line.startswith("Lcom/mobus/ad"):
                continue

            if line.startswith("Lcom/appvador/ad"):
                continue

            
            if ":" and ";" in line:
                count += 1

                cmd = "echo '{0}' >>{1}".format(line,apkoutPutPath)
                os.system(cmd)

        
        apkname = apk.split(".")[0]
        txtname = Path.split("/")[-2]+ "_delete_CFG.txt"

        cmd = "echo {0} {1} >> {2}".format(apkname,count,txtname)
        os.system(cmd)

        csvname = Path.split("/")[-2] + "_delete_CFG.csv"
        
        cmd = "echo {0} >> {1}".format(count,csvname)
        os.system(cmd)

        print "we are handling with {0} ... ".format(apkname)


#deleteAds(oriPath,orioutPutPath)
deleteAds(repPath,repoutPutPath)


print "all work is done!"














