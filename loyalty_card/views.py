from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import re

from linebot.models.responses import MessageQuotaResponse
from loyalty_card.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            mtext=event.message.text
            uid=event.source.user_id
            profile=line_bot_api.get_profile(uid)
            name=profile.display_name
            pic_url=profile.picture_url
            message = []
            stage = ""
            ##### Change Stage #####
            if re.match("GitHub工作坊", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="GitHub工作坊")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "GitHub工作坊")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("簡歷工作坊", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="簡歷工作坊")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "簡歷工作坊")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("火鍋大會", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="火鍋大會")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "火鍋大會")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("抽彤瑾", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="抽彤瑾")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "抽彤瑾")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("你麻糬了", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="你麻糬了")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "你麻糬了")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("點數查詢", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="點數查詢")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "點數查詢")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點總和'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("jolinon", event.message.text): ##### 開啟抽彤瑾管理員系統 #####
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="抽彤瑾管理員系統")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "抽彤瑾管理員系統")
                message.append(TextSendMessage(text='//已進入 「抽彤瑾管理員系統」'))
                message.append(TextSendMessage(text='周彤瑾，請你輸入有玩「抽彤瑾」的人的學號，如果你要關掉「抽彤瑾管理員系統」請輸入"jolinoff"，不然直接按下面的選單也可。'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("jolinoff", event.message.text): ##### 關閉抽彤瑾管理員系統 #####
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="default")
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "default")
                message.append(TextSendMessage(text='//已關閉「抽彤瑾管理員系統」\n掰掰周彤瑾'))
                line_bot_api.reply_message(event.reply_token,message)
            else:
                ##### 查詢集點狀況 #####
                if User_Info.objects.filter(uid=uid).exists()==True:
                    user_info = User_Info.objects.filter(uid=uid)
                    for user in user_info:
                        stage = user.stage
                    if re.match(stage, "簡歷工作坊"):
                        if Sheet.objects.filter(student_id = event.message.text).exists() == False:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                        elif Sheet.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Sheet.objects.filter(student_id = event.message.text)
                            message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                        message.append(TextSendMessage(text='//查詢「簡歷工作坊」集點狀況'))
                    elif re.match(stage, "抽彤瑾"):
                        if CCK.objects.filter(student_id = event.message.text).exists() == False:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                        elif CCK.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = CCK.objects.filter(student_id = event.message.text)
                            message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                        message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    elif re.match(stage, "火鍋大會"):
                        if Hotpot.objects.filter(student_id = event.message.text).exists() == False:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                        elif Hotpot.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Hotpot.objects.filter(student_id = event.message.text)
                            message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                        message.append(TextSendMessage(text='//查詢「火鍋大會」集點狀況'))
                    elif re.match(stage, "GitHub工作坊"):
                        if Github.objects.filter(student_id = event.message.text).exists() == False:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                        elif Github.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Github.objects.filter(student_id = event.message.text)
                            message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                        message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    elif re.match(stage, "你麻糬了"):
                        if Machi.objects.filter(student_id = event.message.text).exists() == False:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                        elif Machi.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Machi.objects.filter(student_id = event.message.text)
                            message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                        message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    elif re.match(stage, "點數查詢"):
                        sum = 0
                        if Sheet.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Sheet.objects.filter(student_id = event.message.text)
                            sum += student_info[0].getpoint
                        if CCK.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = CCK.objects.filter(student_id = event.message.text)
                            sum += student_info[0].getpoint
                        if Hotpot.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Hotpot.objects.filter(student_id = event.message.text)
                            sum += student_info[0].getpoint
                        if Github.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Github.objects.filter(student_id = event.message.text)
                            sum += student_info[0].getpoint
                        if Machi.objects.filter(student_id = event.message.text).exists() == True:
                            student_info = Machi.objects.filter(student_id = event.message.text)
                            sum += student_info[0].getpoint
                        if sum == 0:
                            message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名任一資工感化院活動\n2.未參加任一資工感化院活動\n3.輸入非學號字元\n**如有任何問題請聯絡交大資工系學會粉專'%(event.message.text)))
                        else:
                            message.append(TextSendMessage(text='學號%s 共獲得%s點'%(event.message.text, sum)))
                        message.append(TextSendMessage(text='//查詢「總點數」'))
                    elif re.match(stage, "抽彤瑾管理員系統"):
                        CCK.objects.create(student_id = event.message.text, getpoint = 1)
                        message.append(TextSendMessage(text='//導入資料庫成功'))
                        message.append(TextSendMessage(text='周彤瑾，請輸入下一個玩的人的學號，或是輸入"jolinoff"把「抽彤瑾管理員系統」關掉'))
                    # Robot Reply
                    elif re.match(stage, "default"):
                        message.append(TextSendMessage(text='感謝您使用資工感化院集點卡，請按選單上的選項進行點數查詢!!'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif User_Info.objects.filter(uid=uid).exists()==False:
                    message.append(TextSendMessage(text='感謝您使用資工感化院集點卡，請按選單上的選項進行點數查詢!!'))
                    line_bot_api.reply_message(event.reply_token,message)




        return HttpResponse()
    else:
        return HttpResponseBadRequest()