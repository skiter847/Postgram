from django.conf import settings


def check_exists(bot, name):
    """
    Если чата не существует будет вызвана ошибка и функцию вернет None,
    в ином случает возвараем обьект Chat который содержит онформацию о чате
    """
    try:
        return bot.get_chat(name)
    except Exception as e:
        pass


def check_bot_permissions(bot, chat_id):
    has_perm = False
    member = bot.get_chat_member(chat_id, settings.BOT_ID)
    if all([member.can_post_messages, member.can_edit_messages, member.can_delete_messages]):
        has_perm = True

    return has_perm
