<template>
    <div>
        <span class="server-status" :style="{ color : serverColor}"> {{ serverStatus }} </span>
        <span class="load-status">
            <!---<template v-if="loadStatus"><img src="../assets/spinner.gif" alt=""></template>--->
        </span>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                serverStatus: 'Loading...',
                serverColor: 'gray',
                loadStatus: true,
                host: window.location.hostname
            }
        },
        created () {
            this.checkStatus()
        },
        updated () {
            this.checkStatus()
        },
        methods: {
            checkStatus: function () {
                let url = 'http://' + this.host + ':5000/test'
                this.$http.get(url).then( response => {
                    this.serverStatus = '✓ The API is available'
                    this.serverColor = 'green'
                }, response => {
                    this.serverStatus = 'X The API is not available'
                    this.serverColor = 'red'
                })
            }
        }
    }
</script>