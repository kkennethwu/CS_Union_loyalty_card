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
            if re.match("新增會員資料", event.message.text):
                if User_Info.objects.filter(uid=uid).exists()==False:
                    User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext, stage=0, point=1)
                    message.append(TextSendMessage(text='會員資料新增完畢'))
                elif User_Info.objects.filter(uid=uid).exists()==True:
                    message.append(TextSendMessage(text='已經有建立會員資料囉'))
                    user_info = User_Info.objects.filter(uid=uid)
                    for user in user_info:
                        info = 'UID=%s\nNAME=%s\n大頭貼=%s\npoint=%s'%(user.uid,user.name,user.pic_url,user.point)
                        message.append(TextSendMessage(text=info))
                line_bot_api.reply_message(event.reply_token,message)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()