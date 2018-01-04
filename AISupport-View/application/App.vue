<template>
    <div id="support-box">
        <div class="wrapper">
            <div id="status">
                <client ref="client" @messageReceived="getMessage($event)" @requestFailed="getError($event)"></client>
            </div>
            <div id="conversation">
                <message-board ref="messageBoard"></message-board>
            </div>
            <div id="input">
                <input type="text" placeholder="Start typing here..." class="text" name="message" @keyup.enter="sendInput()" v-model="input">
            </div>
        </div>
    </div>
</template>


<script>
    import Client from './components/Client.vue'
    import MessageBoard from './components/MessageBoard.vue'
    export default {
        data () {
            return {
                input: ''
            }
        },
        methods: {
            sendInput ()  {
                // Send to client
                this.$refs.client.makeRequest('question', this.input)
                // Push to Message Board
                this.$refs.messageBoard.printMessage('You', this.input)
                // Clear input
                this.input = ' '
            },
            getMessage (msg) {
                // Push to Message Board
                this.$refs.messageBoard.printMessage('Support', msg)
            },
            getError (errorMsg) {
                alert(errorMsg)
            }
        },
        components: {
            Client,
            MessageBoard
        }
    }
</script>

<style lang="scss">
    @import 'style/main';
</style>