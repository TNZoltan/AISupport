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
                console.log('Status check began')
                this.loadStatus = true
                let url = 'http://' + this.host + ':5000/test'
                console.log('Host is '+ url)
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
            }
        }
    }
</script>