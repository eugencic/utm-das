<template>
    <div>
        <p>{{ result }}</p>
        <img src = "../assets/qrcodes/engleza/qrcode.png"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'engleza',
    data: () => ({
        timer: null,
        result: "Limba Engleza - Prezenta"
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