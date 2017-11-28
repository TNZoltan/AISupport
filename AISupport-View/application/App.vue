<template>
    <div id="wrapper">
        <div id="status">
            <client></client>
        </div>
        <div id="conversation">
            <div class="messages">

            </div>
        </div>
        <div id="input">
            <input type="text" placeholder="Start typing here..." class="text" name="message">
        </div>
    </div>
</template>


<script>
    import Client from './functions/Client.vue'
    export default {
        data () {
            return {
                test: 'Start. Fetch message in 2 seconds'
            }
        },
        created () {

        },
        components: {
            'client' : Client
        }
    }
</script>

<style lang="scss">
    @import 'style/main';
</style>