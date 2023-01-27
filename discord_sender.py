# importing base libraries
import requests

# import specific libraries for discord

# importing internal modules
import authorization_secrets

def send_message_to_chanel(chanel_url, user_id, content_text):
    auth = {
    'authorization': user_id
    }
    
    msg = {
    'content': content_text
    }

    requests.post(chanel_url, headers = auth, data = msg)

if __name__ == '__main__':
    chanel_url = authorization_secrets.chanel_url
    user_id = authorization_secrets.user_id

    print('Hello there!\nTo exit press press Enter.\nTo send message enter text:', end='')
    content_text = input()
    
    if content_text:
        send_message_to_chanel(chanel_url, user_id, content_text)
    else:
        print('See you next time!')
