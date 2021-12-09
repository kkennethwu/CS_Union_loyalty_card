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
            # if isinstance(event, MessageEvent):
            #     mtext=event.message.text
            #     message=[]
            #     message.append(TextSendMessage(text=mtext))
            #     line_bot_api.reply_message(event.reply_token,message)
            mtext=event.message.text
            uid=event.source.user_id
            profile=line_bot_api.get_profile(uid)
            name=profile.display_name
            pic_url=profile.picture_url
            message = []
            stage = ""
            # if re.match("新增會員資料", event.message.text):
            #     if User_Info.objects.filter(uid=uid).exists()==False:
            #         User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage='建立會員中')
            #     elif User_Info.objects.filter(uid=uid).exists()==True:
            #         message.append(TextSendMessage(text='已經有建立會員資料囉'))
            #         user_info = User_Info.objects.filter(uid=uid)
            #         for user in user_info:
            #             info = 'UID=%s\nNAME=%s\n大頭貼=%s\nStage=%s\nPoint=%s'%(user.uid,user.name,user.pic_url,user.stage)
            #             message.append(TextSendMessage(text=info))
            #     line_bot_api.reply_message(event.reply_token,message)
            if re.match("GitHub工作坊", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="GitHub工作坊", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "GitHub工作坊")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("簡歷工作坊", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="簡歷工作坊", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "簡歷工作坊")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("火鍋大會", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="火鍋大會", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "火鍋大會")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("抽彤瑾", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="抽彤瑾", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "抽彤瑾")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("你麻糬了", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="你麻糬了", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "你麻糬了")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點狀況'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("點數查詢", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="點數查詢", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "點數查詢")
                message.append(TextSendMessage(text='//請輸入學號以查詢集點總和'))
                line_bot_api.reply_message(event.reply_token,message)


            if User_Info.objects.filter(uid=uid).exists()==True:
                user_info = User_Info.objects.filter(uid=uid)
                for user in user_info:
                    stage = user.stage
                if re.match(stage, "簡歷工作坊"):
                    message.append(TextSendMessage(text='//查詢「簡歷工作坊」集點狀況'))
                    if Sheet.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                    elif Sheet.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Sheet.objects.filter(student_id = event.message.text)
                        message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                elif re.match(stage, "抽彤瑾"):
                    message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    if CCK.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                    elif CCK.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = CCK.objects.filter(student_id = event.message.text)
                        message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                elif re.match(stage, "火鍋大會"):
                    message.append(TextSendMessage(text='//查詢「火鍋大會」集點狀況'))
                    if Hotpot.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                    elif Hotpot.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Hotpot.objects.filter(student_id = event.message.text)
                        message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                elif re.match(stage, "GitHub工作坊"):
                    message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    if Github.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                    elif Github.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Github.objects.filter(student_id = event.message.text)
                        message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                elif re.match(stage, "你麻糬了"):
                    message.append(TextSendMessage(text='//查詢「抽彤瑾」集點狀況'))
                    if Machi.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='學號%s 獲得0點\n可能為以下狀況:\n1.未報名\n2.未參加\n3.輸入非學號字元'%(event.message.text)))
                    elif Machi.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Machi.objects.filter(student_id = event.message.text)
                        message.append(TextSendMessage(text='學號%s 已獲得%s點'%(event.message.text, student_info[0].getpoint)))
                line_bot_api.reply_message(event.reply_token,message)





        return HttpResponse()
    else:
        return HttpResponseBadRequest()