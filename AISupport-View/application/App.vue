<template>
    <div id="wrapper">
        <div id="status">
            <client ref="client" @messageReceived="printMessage($event)" @requestFailed="printError()"></client>
        </div>
        <div id="conversation">
            <div class="messages">

            </div>
        </div>
        <div id="input">
            <input type="text" placeholder="Start typing here..." class="text" name="message" @keyup.enter="sendInput()" v-model="input">
        </div>
    </div>
</template>


<script>
    import Client from './functions/Client.vue'
    export default {
        data () {
            return {
                input: ''
            }
        },
        methods: {
            sendInput ()  {
                this.$refs.client.makeRequest('question', this.input)
                this.input = ' '
            },
            printMessage (msg) {
                alert(msg)
            },
            printError () {
                alert('We are sorry. There seems to be a server error.')
            }
        },
        components: {
            'client' : Client
        }
    }
</script>

<style lang="scss">
    @import 'style/main';
</style>