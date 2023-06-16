from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror1{CMD_SUFFIX}', f'm1{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror1{CMD_SUFFIX}', f'qm1{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl1{CMD_SUFFIX}', f'y1{CMD_SUFFIX}']
        self.LeechCommand = [f'leech1{CMD_SUFFIX}', f'l1{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech1{CMD_SUFFIX}', f'ql1{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech1{CMD_SUFFIX}', f'yl1{CMD_SUFFIX}']
        self.CloneCommand = f'clone1{CMD_SUFFIX}'
        self.CountCommand = f'count1{CMD_SUFFIX}'
        self.DeleteCommand = f'del1{CMD_SUFFIX}'
        self.CancelMirror = f'cancel1{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancelallbot']
        self.ListCommand = f'list1{CMD_SUFFIX}'
        self.SearchCommand = f'search1{CMD_SUFFIX}'
        self.StatusCommand = [f'status1{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'sall']
        self.UsersCommand = f'users1{CMD_SUFFIX}'
        self.AuthorizeCommand = f'authorize1{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauthorize1{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo1{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo1{CMD_SUFFIX}'
        self.PingCommand = ['ping', 'p']
        self.RestartCommand = [f'restart1{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = f'stats1{CMD_SUFFIX}'
        self.HelpCommand = f'help1{CMD_SUFFIX}'
        self.LogCommand = f'log1{CMD_SUFFIX}'
        self.ShellCommand = f'shell1{CMD_SUFFIX}'
        self.EvalCommand = f'eval1{CMD_SUFFIX}'
        self.ExecCommand = f'exec1{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals1{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting1{CMD_SUFFIX}'
        self.UserSetCommand = f'usetting1{CMD_SUFFIX}'
        self.BtSelectCommand = f'btsel1{CMD_SUFFIX}'
        self.RssCommand = f'rss1{CMD_SUFFIX}'
        self.CategorySelect = f'catsel1{CMD_SUFFIX}'
        self.RmdbCommand = f'rmdb1{CMD_SUFFIX}'
        self.Broadcast = f'broadcast1{CMD_SUFFIX}'
        self.CopysCommand = f'copys1{CMD_SUFFIX}'


BotCommands = _BotCommands()
