module.exports = async (bot,message,args,argsF) => {
    return message.reply({
        content: "Понг
    });
    
};
module.exports.names = ["ping"];
module.exports.interaction = {
    name: 'ping',
    description: 'Ответить на сообщение "Понг!"',
    defaultPermission: true
};
