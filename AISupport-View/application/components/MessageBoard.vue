<template>
    <div id="messages" ref="messages" v-chat-scroll>
        <div v-for="message in messages" class="message-wrap">
            <div class="message" :class="message.sender">
                <div class="sender" v-text="message.sender"></div>
                <div class="text" v-text="message.text"></div>
                <template v-if="message.link">
                    <div class="link">
                        <a :href="message.link">{{ message.link }}</a>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    import { formatMsg } from './formatters'
    export default {
        name: 'message-board',
        data () {
            return {
                messages: []
            }
        },
        methods: {
            printMessage (sender, msg) {
                let msgObject = formatMsg(msg)
                this.messages.push({
                    sender: sender,
                    text: msgObject.text,
                    link: msgObject.link
                })
            }
        }
    }
</script>

<style scoped>

</style>