package com.example.kidsafe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.StrictMode;
import android.text.TextUtils;
import android.util.Log;
import android.widget.Toast;

import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;
import com.google.gson.JsonObject;

import org.json.JSONObject;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Objects;

public class LoginActivity extends AppCompatActivity {

    TextInputEditText username, password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        Objects.requireNonNull(getSupportActionBar()).setTitle("Log In");

        username = findViewById(R.id.textInputEditText);
        password = findViewById(R.id.textInputEditText1);

        MaterialButton logInButton = findViewById(R.id.materialButton1);

        logInButton.setOnClickListener(view -> logIn());

    }

    private void logIn() {

        HttpURLConnection con = null;
        try {
            JsonObject postData = new JsonObject();
            postData.addProperty("username", Objects.requireNonNull(username.getText()).toString());
            postData.addProperty("password", Objects.requireNonNull(password.getText()).toString());


            SharedPreferences sh = getSharedPreferences("MySharedPref", Context.MODE_PRIVATE);
            String hostAdr = sh.getString("HOST_ADR", "");

            String url = hostAdr + "/login";
            URL obj = new URL(url);
            con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("POST");
            con.setConnectTimeout(2000);
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);
            con.setDoInput(true);
            con.setChunkedStreamingMode(0);


            OutputStream out = new BufferedOutputStream(con.getOutputStream());
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(
                    out, StandardCharsets.UTF_8));
            writer.write(postData.toString());
            writer.flush();

            int responseCode = con.getResponseCode();

            if (responseCode == 500) {
                Toast toast = Toast.makeText(LoginActivity.this, "Username Not Found", Toast.LENGTH_SHORT);
                toast.getView().setBackgroundResource(R.drawable.toast_red);
                toast.show();
                return;
            }

            BufferedReader rd = new BufferedReader(new InputStreamReader(
                    con.getInputStream()));
            String line;
            String idnp = "", rol = "", statusCode = "";

            while ((line = rd.readLine()) != null) {
                int index1, index2, index3, index4;
                index1 = line.indexOf('\'');
                index2 = line.indexOf('\'', index1 + 1);
                index3 = line.indexOf('\'', index2 + 1);
                index4 = line.indexOf('\'', index3 + 1);

                idnp = line.substring(index1 + 1, index2);
                rol = line.substring(index3 + 1, index4);
                statusCode = line.substring(index4 + 3, index4 + 6);
            }

            if (Objects.equals(statusCode, "401")) {
                Toast toast = Toast.makeText(LoginActivity.this, "Wrong Password", Toast.LENGTH_SHORT);
                toast.getView().setBackgroundResource(R.drawable.toast_red);
                toast.show();
                return;
            }

            if (Objects.equals(statusCode, "200")) {

                SharedPreferences sharedPreferences = getSharedPreferences("MySharedPref", MODE_PRIVATE);
                SharedPreferences.Editor myEdit = sharedPreferences.edit();
                myEdit.putString("IDNP", idnp);
                myEdit.apply();

                Toast toast = Toast.makeText(LoginActivity.this, "User logged in successfully", Toast.LENGTH_LONG);
                toast.getView().setBackgroundResource(R.drawable.toast_blue);
                toast.show();

                if (Objects.equals(rol, "elev")) {
                    startActivity(new Intent(LoginActivity.this, StudentActivity.class));
                } else if (Objects.equals(rol, "parinte")) {
                    startActivity(new Intent(LoginActivity.this, ParentActivity.class));
                }

                finish();
            }

        } catch (Exception e) {
            Toast toast = Toast.makeText(LoginActivity.this, "Network Connection Error", Toast.LENGTH_SHORT);
            toast.getView().setBackgroundResource(R.drawable.toast_red);
            toast.show();
        } finally {
            if (con != null) {
                con.disconnect();
            }
        }

    }
}