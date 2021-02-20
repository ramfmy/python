def send_invitation(experts):
    '''发送邀请函'''
    for expert in experts:
        print(expert + '，您好，现邀请您参加 XX 研讨会...')


expertss = ['袁孝楠', '黄莉莉']
send_invitation(expertss)
