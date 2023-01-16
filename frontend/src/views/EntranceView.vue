<template>
    <div>
        <p>{{ result }}</p>
        <img src = "../assets/qrcodes/entrance/qrcode.png"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'entrance',
    data: () => ({
        timer: null,
        result: "Scan the QR Code when you enter and leave the school"
    }),
    // methods: {
    //     getMessage() {
    //         const URL = 'http://localhost:5000/entrance'
    //         axios.get(URL).then(response => this.result = response.data)
    //     }
    // },
    // mounted() {
    //     this.getMessage()
    // }
}
</script>