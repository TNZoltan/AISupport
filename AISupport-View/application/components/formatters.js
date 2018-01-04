export const formatMsg = function (msg) {
    let linkFound = msg.match(/\[link\].*\[\/link]/g)
    console.log(linkFound)
    if (linkFound) {
        return {
            'text': msg.replace(linkFound[0], '') , 'link': linkFound[0].slice(6, linkFound[0].length-7)
        }
    } else {
        return {
            'text': msg, 'link': false
        }
    }
}

