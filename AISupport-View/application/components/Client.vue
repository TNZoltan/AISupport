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
        name: 'client',
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
            makeRequest: function (type, question = null) {
                this.loadStatus = true
                let url = 'http://' + this.host + ':5000/api/talk'
                let formData = new FormData();

                formData.append('type', type);
                formData.append('question', question);

                let body = JSON.stringify({
                    type: type ,
                    question: question
                })
                this.$http.post(url, formData).then( response => {
                    setTimeout(() => {
                        console.log(response)
                        this.loadStatus = false
                        this.$emit('messageReceived', response.body.msg)
                    },300)
                }, response => {
                    console.log(response)
                    this.loadStatus = false
                    this.$emit('requestFailed', 'We are sorry. There seems to be a server error.')
                })
            }
        }
    }
</script>