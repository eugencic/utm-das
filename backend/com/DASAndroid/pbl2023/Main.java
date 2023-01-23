package com.DASAndroid.pbl2023;

import org.json.JSONException;
import org.json.JSONObject;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.IOException;
import java.math.BigInteger;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PublicKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.RSAPublicKeySpec;
import java.util.HashMap;

import com.DASAndroid.pbl2023.Encription;
import com.DASAndroid.pbl2023.Users;
import com.DASAndroid.pbl2023.Parinte;

public class Main {
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException, InvalidKeySpecException, IllegalBlockSizeException, NoSuchPaddingException, BadPaddingException, InvalidKeyException, JSONException {
        // get Public key RSA
        HashMap<String, String> publicKey_map = Encription.getPublicKey();
        System.out.println(publicKey_map);
        BigInteger n = new BigInteger(publicKey_map.get("public_n"));
        BigInteger e = new BigInteger( publicKey_map.get("public_e"));
        RSAPublicKeySpec publickey = new RSAPublicKeySpec(n , e);

        // Get Qr Code
        System.out.println(Encription.getQr());

        // message to send :
        String idnp = "123456789101";
        String message = Encription.getQr() + idnp;
        KeyFactory factory = KeyFactory.getInstance("RSA");
        PublicKey pub = factory.generatePublic(publickey);

        // encript :
        byte[] encripted = Encription.encrypt(message, pub);
        String encripted_string = new String(encripted, "ISO-8859-1");
        System.out.println(encripted_string);

        // Send
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("secretkey",encripted_string);
        Encription.postEntranceMessage(sender_jo);

        // Check loghin
        Users.postUserLoghInMessage(Users.createUserJson("laur", "laur"));

        // Create new parinte and new child
        // Din cauza la db , cream intai parintele apoi elevul , care va trebui sa aiba trimitere catre numele parintelui sau:
//        Users.postCreateNewParinte(Users.createNewParinteJson("parintenou", "parintenou", "123456789119", "Grigore Vasilean", "P. Rares", "grisaVas@mail.com"));
//        Users.postCreateNewElev(Users.createNewElevJson("laur1","laur1", "123456789000","Ion Vasile", "12", "P. Rares", "Grigore Vasilean"));

        // Adaugam noi copii :
//        Parinte.postNewChildAdd(Parinte.createNewChildJson("Ion Vasile", "Grigore Vasilean"));

    }
}
