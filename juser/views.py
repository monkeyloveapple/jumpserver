def perm_rule_add(assets_obj, asset_groups_obj, users_obj,
                  user_groups_obj, roles_obj, rule_name, rule_comment):
    """
    add rule page
    添加授权API,参数为object 如：users_obj = [User.objects.get(id=user_id) for user_id in users_select]
    """
    try:
        rule = PermRule(name=rule_name, comment=rule_comment)
        rule.save()
        rule.user = users_obj
        rule.user_group = user_groups_obj
        rule.asset = assets_obj
        rule.asset_group = asset_groups_obj
        rule.role = roles_obj
        rule.save()

        msg = u"添加授权规则：%s" % rule.name
        res = {'result': True, 'Msg': msg}
        return json.dumps(res)
    except ServerError, e:
        error = e
        logger.info(error)
        res = {'result': False, 'Msg': error}
        return json.dumps(res)


def app_send_mail(user, app, check_res, mail_type, host_url):
    """
    check app send mail
    发送审批邮件
    mail_type == "user" or "checker"
    """
    if mail_type == "user":
        mail_title = u'堡垒机权限申请审批结果'
        url = host_url+reverse('follow_app')
        mail_msg = u"""
        Hi, %s
            您的堡垒机权限申请: %s,
            %s,
            请登录系统查看:
            %s
        """ % (user.name, app.app_name, check_res, url)
    else:
        mail_title = u'堡垒机权限申请审批'
        url = host_url+reverse('check_app')
        mail_msg = u"""
        Hi, %s
            堡垒机权限申请: %s,
            请您登录系统审批:
            %s
        """ % (user.name, app.app_name, url)
    send_mail(mail_title, mail_msg, MAIL_FROM, [user.email], fail_silently=False)
