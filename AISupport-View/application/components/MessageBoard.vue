<template>
    <div id="messages">
        <div v-for="message in messages">
            <span v-text="message.sender"></span>: <span v-text="message.text"></span>
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