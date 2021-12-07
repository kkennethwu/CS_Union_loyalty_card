from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import re
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
                message.append(TextSendMessage(text='請輸入學號'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("簡歷工作坊", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="簡歷工作坊", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "簡歷工作坊")
                message.append(TextSendMessage(text='請輸入學號'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("火鍋大會", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="火鍋大會", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "火鍋大會")
                message.append(TextSendMessage(text='請輸入學號'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("抽彤瑾", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="抽彤瑾", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "抽彤瑾")
                message.append(TextSendMessage(text='請輸入學號'))
                line_bot_api.reply_message(event.reply_token,message)
            elif re.match("你麻糬了", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage="你麻糬了", point=0)
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    User_Info.objects.filter(uid=uid).update(stage = "你麻糬了")
                message.append(TextSendMessage(text='請輸入學號'))
                line_bot_api.reply_message(event.reply_token,message)




            if User_Info.objects.filter(uid=uid).exists()==True:
                user_info = User_Info.objects.filter(uid=uid)
                for user in user_info:
                    stage = user.stage
                if re.match(stage, "簡歷工作坊"):
                    message.append(TextSendMessage(text='stage in sheet\n'))
                    if Sheet.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='您尚未報名\n'))
                    elif Sheet.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Sheet.objects.filter(student_id = event.message.text)
                        for s in student_info:
                            if s.getpoint == 0:
                                Sheet.objects.filter(student_id = event.message.text).update(getpoint = 2)
                                message.append(TextSendMessage(text='已集點成功 獲得兩點\n'))
                            else:
                                message.append(TextSendMessage(text='已經集點過囉 現有兩點\n'))
                elif re.match(stage, "GitHub工作坊"):
                    message.append(TextSendMessage(text='stage in github'))
                    if Github.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='您尚未報名\n'))
                    elif Github.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Github.objects.filter(student_id = event.message.text)
                        for s in student_info:
                            if s.getpoint == 0:
                                Github.objects.filter(student_id = event.message.text).update(getpoint = 2)
                                message.append(TextSendMessage(text='已集點成功 獲得兩點\n'))
                            else:
                                message.append(TextSendMessage(text='已經集點過囉 現有兩點\n'))
                elif re.match(stage, "火鍋大會"):
                    message.append(TextSendMessage(text='stage in 火鍋大會'))
                    if Hotpot.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='您尚未報名\n'))
                    elif Hotpot.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Hotpot.objects.filter(student_id = event.message.text)
                        for s in student_info:
                            if s.getpoint == 0:
                                Hotpot.objects.filter(student_id = event.message.text).update(getpoint = 2)
                                message.append(TextSendMessage(text='已集點成功 獲得兩點\n'))
                            else:
                                message.append(TextSendMessage(text='已經集點過囉 現有兩點\n'))
                elif re.match(stage, "你麻糬了"):
                    message.append(TextSendMessage(text='stage in 你麻糬了'))
                    if Hotpot.objects.filter(student_id = event.message.text).exists() == False:
                        message.append(TextSendMessage(text='您尚未報名\n'))
                    elif Hotpot.objects.filter(student_id = event.message.text).exists() == True:
                        student_info = Hotpot.objects.filter(student_id = event.message.text)
                        for s in student_info:
                            if s.getpoint == 0:
                                Hotpot.objects.filter(student_id = event.message.text).update(getpoint = 2)
                                message.append(TextSendMessage(text='已集點成功 獲得兩點\n'))
                            else:
                                message.append(TextSendMessage(text='已經集點過囉 現有兩點\n'))
                elif re.match(stage, "抽彤瑾"):
                    message.append(TextSendMessage(text='stage in 抽彤瑾'))
                    # if Sheet.objects.filter(student_id = event.message.text).exists() == False:
                    #     message.append(TextSendMessage(text='您尚未報名\n'))
                    # elif Sheet.objects.filter(student_id = event.message.text).exists() == True:
                    #     student_info = Sheet.objects.filter(student_id = event.message.text)
                    #     for s in student_info:
                    #         if s.getpoint == 0:
                    #             Sheet.objects.filter(student_id = event.message.text).update(getpoint = 2)
                    #             message.append(TextSendMessage(text='已集點成功 獲得兩點\n'))
                    #         else:
                    #             message.append(TextSendMessage(text='已經集點過囉 現有兩點\n'))
                line_bot_api.reply_message(event.reply_token,message)





        return HttpResponse()
    else:
        return HttpResponseBadRequest()