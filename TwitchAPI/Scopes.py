class Scopes:

    __scopes = []

    def __init__(self, user_read=False, user_blocks_edit=False, user_blocks_read=False, user_follows_edit=False,
                 channel_read=False, channel_editor=False, channel_commercial=False, channel_stream=False,
                 channel_subscriptions=False, user_subscriptions=False, channel_check_subscription=False,
                 chat_login=False):
        self.__scopes = [scope for scope, val in locals().items() if scope is not "self" and val]

    def __str__(self):
        return "+".join(self.__scopes)
