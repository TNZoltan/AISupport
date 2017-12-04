<template>
    <div>
        <span class="server-status" :style="{ color : serverColor}"> {{ serverStatus }} </span>
        <span class="load-status">
            <template v-if="loadStatus"><img src="../assets/spinner.gif" alt=""></template>
        </span>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                serverStatus: 'Loading...',
                serverColor: 'gray',
                serverChecked: false,
                loadStatus: false,
                host: window.location.hostname
            }
        },
        mounted () {
            if (!this.serverChecked) {
                this.checkStatus()
            }
        },
        methods: {
            checkStatus: function () {
                this.loadStatus = true
                let url = 'http://' + this.host + ':5000/api/test'
                this.$http.get(url).then( response => {
                    this.serverStatus = '✓ The API is available'
                    this.serverColor = 'green'
                    this.loadStatus = false
                }, response => {
                    this.serverStatus = 'X The API is not available'
                    this.serverColor = 'red'
                    this.loadStatus = false
                })
                this.serverChecked = true
            },
            getMessage: function (type, question = null) {
                this.loadStatus = true
                let url = 'http://' + this.host + ':5000/api/talk'
                let body = {
                    type: type ,
                    question: question
                }
                console.log(body)
                this.$http.put(url, body).then( response => {
                    this.loadStatus = false
                    return response.body.message
                }, response => {
                    this.loadStatus = false
                    return false
                })
            }
        }
    }
</script>