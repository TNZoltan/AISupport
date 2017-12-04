<template>
    <div id="wrapper">
        <div id="status">
            <client ref="client"></client>
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
                console.log(this.$refs.client.getMessage('question',this.input))
                this.input = ' '
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