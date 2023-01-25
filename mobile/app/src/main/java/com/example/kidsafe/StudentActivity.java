package com.example.kidsafe;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.ImageButton;
import android.widget.Toast;

import androidx.activity.result.ActivityResultLauncher;
import androidx.appcompat.app.AppCompatActivity;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import com.journeyapps.barcodescanner.ScanContract;
import com.journeyapps.barcodescanner.ScanOptions;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.lang.reflect.Type;
import java.math.BigInteger;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.spec.RSAPublicKeySpec;
import java.util.HashMap;
import java.util.Objects;

import javax.crypto.Cipher;

public class StudentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student);
        Objects.requireNonNull(getSupportActionBar()).setTitle("Menu");

        ImageButton scanQr = findViewById(R.id.imageButton1);

        scanQr.setOnClickListener(view -> scanCode());
    }

    private void scanCode() {
        ScanOptions options = new ScanOptions();
        options.setPrompt("");
        options.setBeepEnabled(false);
        options.setOrientationLocked(true);
        options.setCaptureActivity(CaptureAct.class);
        qrLauncher.launch(options);
    }

    ActivityResultLauncher<ScanOptions> qrLauncher = registerForActivityResult(new ScanContract(), result -> {
        if (result.getContents() != null) {

            SharedPreferences sh = getSharedPreferences("MySharedPref", Context.MODE_PRIVATE);
            String hostAdr = sh.getString("HOST_ADR", "");
            String idnp = sh.getString("IDNP", "");

            HashMap<String, String> publicKey_map = getPublicKey();
            BigInteger n = new BigInteger(Objects.requireNonNull(publicKey_map.get("public_n")));
            BigInteger e = new BigInteger(Objects.requireNonNull(publicKey_map.get("public_e")));
            RSAPublicKeySpec publickey = new RSAPublicKeySpec(n, e);


            PublicKey pub;
            try {
                KeyFactory factory = KeyFactory.getInstance("RSA");
                pub = factory.generatePublic(publickey);
            } catch (Exception e1) {
                return;
            }

            String text = result.getContents() + "/" + idnp;

            // encript :
            byte[] encripted = encrypt(text, pub);
            String encripted_string = new String(encripted, StandardCharsets.ISO_8859_1);

            JSONObject sender_jo = new JSONObject();
            try {
                sender_jo.put("secretkey", encripted_string);
            } catch (JSONException ex) {
                return;
            }

            postSendJson(sender_jo);

        }


    });

    public HashMap<String, String> getPublicKey() {
        try {

            SharedPreferences sh = getSharedPreferences("MySharedPref", Context.MODE_PRIVATE);
            String hostAdr = sh.getString("HOST_ADR", "");

            String url = hostAdr + "/publickey";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("GET");
            int responseCode = con.getResponseCode();
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
//        System.out.println(response.toString());
            String sjson = response.toString();
            Gson gson = new Gson();
            Type type = new TypeToken<HashMap<String, String>>() {
            }.getType();
            HashMap<String, String> map = gson.fromJson(sjson, type);
            return map;
        } catch (Exception e) {
            return null;
        }
    }

    public byte[] encrypt(String data, PublicKey publicKey) {
        try {
            Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
            cipher.init(Cipher.ENCRYPT_MODE, publicKey);
            return cipher.doFinal(data.getBytes(StandardCharsets.ISO_8859_1));
        } catch (Exception e) {
            return null;
        }
    }

    public void postSendJson(JSONObject jo) {
        try {

            SharedPreferences sh = getSharedPreferences("MySharedPref", Context.MODE_PRIVATE);
            String hostAdr = sh.getString("HOST_ADR", "");

            String url = hostAdr + "/receiveqr";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            String json = jo.toString();
            byte[] postData = json.getBytes();
            con.setDoOutput(true);
            try (DataOutputStream wr = new DataOutputStream(con.getOutputStream())) {
                wr.write(postData);
            }
            int responseCode = con.getResponseCode();
            System.out.println("Response Code : " + responseCode);
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
        } catch (Exception ignored) {

        }
    }

    @Override
    public void onBackPressed() {
    }
}