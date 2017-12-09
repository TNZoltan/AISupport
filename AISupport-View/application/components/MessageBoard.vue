<template>
    <div id="messages" ref="messages">
        <div v-for="message in messages" class="message" :class="message.sender">
            <div class="sender" v-text="message.sender"></div> <div class="text" v-text="message.text"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'message-board',
        data () {
            return {
                messages: []
            }
        },
        methods: {
            printMessage (sender, text) {
                this.messages.push({
                    sender: sender,
                    text: text
                })
            }
        }
    }
</script>

<style scoped>

</style>