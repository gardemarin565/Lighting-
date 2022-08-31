module.exports = async (bot,message,args,argsF) => {
    //args - это массив аргументов. Например g/ping 0 1 2 tEsT | args[0]="0", args[1]="1", args[2]="2", args[3]="test" . А так-же argsF[3]=="tEsT"
    return message.reply({ //Это команда пинг!
        content: "pong!"
    });
    
};
module.exports.names = ["ping"]; //У неё есть название