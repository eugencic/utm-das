<template>
    <div>
        <p>{{ result }}</p>
        <img src = "../assets/qrcodes/romana/qrcode.png"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'entrance',
    data: () => ({
        timer: null,
        result: "Romana - Prezenta"
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