class Solution:
    def reformatDate(self, date: str) -> str:
        mon = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        da = date.split()
        build = da[2] + "-"
        build += mon[da[1]] + "-"
        
        day = da[0]
        if len(day) == 3:
            build += "0" + day[0]
        else:
            build += day[0] + day[1]
        
        return build

