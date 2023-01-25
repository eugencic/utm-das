package com.example.kidsafe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.StrictMode;
import android.text.Editable;
import android.text.TextUtils;
import android.text.TextWatcher;
import android.widget.Toast;

import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;
import com.google.gson.JsonObject;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedOutputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SignUpActivity extends AppCompatActivity {

    TextInputEditText etSignUpID;
    TextInputLayout SignUpID;

    TextInputEditText etSignUpPass;
    TextInputLayout SignUpPass;

    TextInputEditText parentID, fullName, email, institution, form, username;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        Objects.requireNonNull(getSupportActionBar()).setTitle("Sign Up as Student");

        etSignUpID = findViewById(R.id.textInputEditText);
        SignUpID = findViewById(R.id.textInputLayout);

        etSignUpPass = findViewById(R.id.textInputEditText1);
        SignUpPass = findViewById(R.id.textInputLayout1);

        parentID = findViewById(R.id.textInputEditText9);
        fullName = findViewById(R.id.textInputEditText2);
        email = findViewById(R.id.textInputEditText3);
        institution = findViewById(R.id.textInputEditText4);
        form = findViewById(R.id.textInputEditText8);
        username = findViewById(R.id.textInputEditText5);

        etSignUpID.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if (charSequence.length() < 13) {
                    SignUpID.setError("ID number is 13 characters long!");
                } else SignUpID.setError(null);
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });

        etSignUpPass.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if (charSequence.length() < 8) {
                    SignUpPass.setError("Minimum 8 characters");
                } else SignUpPass.setError(null);

                Pattern digit = Pattern.compile("[0-9]");
                Pattern special = Pattern.compile("[!@#$%&*()_+=|<>?{}\\[\\]~-]");

                Matcher hasDigit = digit.matcher(charSequence);
                Matcher hasSpecial = special.matcher(charSequence);

                if (!hasSpecial.find()) {
                    SignUpPass.setError("Minimum 1 special character");
                }

                if (!hasDigit.find()) {
                    SignUpPass.setError("Minimum 1 digit");
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });

        MaterialButton signUpButton = findViewById(R.id.materialButton1);

        signUpButton.setOnClickListener(view -> signUp());
    }

    private void signUp() {
        if (SignUpID.getError() == null && SignUpPass.getError() == null &&
                !TextUtils.isEmpty(Objects.requireNonNull(etSignUpID.getText()).toString()) &&
                !TextUtils.isEmpty(Objects.requireNonNull(etSignUpPass.getText()).toString())) {


            HttpURLConnection con = null;
            try {
                JsonObject postData = new JsonObject();
                postData.addProperty("username", Objects.requireNonNull(username.getText()).toString());
                postData.addProperty("password", etSignUpPass.getText().toString());
                postData.addProperty("idnp", etSignUpID.getText().toString());
                postData.addProperty("name_surname", Objects.requireNonNull(fullName.getText()).toString());
                postData.addProperty("clasa", Objects.requireNonNull(form.getText()).toString());
                postData.addProperty("liceu", Objects.requireNonNull(institution.getText()).toString());
                postData.addProperty("parinte", Objects.requireNonNull(parentID.getText()).toString());


                SharedPreferences sh = getSharedPreferences("MySharedPref", Context.MODE_PRIVATE);
                String hostAdr = sh.getString("HOST_ADR", "");

                String url = hostAdr + "/signupelev";
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

                System.out.println(responseCode);
            } catch (Exception e) {
                Toast toast = Toast.makeText(SignUpActivity.this, "Network Connection Error", Toast.LENGTH_SHORT);
                toast.getView().setBackgroundResource(R.drawable.toast_red);
                toast.show();
                return;
            } finally {
                if (con != null) {
                    con.disconnect();
                }
            }


            Toast toast = Toast.makeText(SignUpActivity.this, "User registered successfully", Toast.LENGTH_LONG);
            toast.getView().setBackgroundResource(R.drawable.toast_blue);
            toast.show();

            startActivity(new Intent(SignUpActivity.this, StudentActivity.class));
            finish();
        } else {
            Toast toast = Toast.makeText(SignUpActivity.this, "Sign Up Field Error", Toast.LENGTH_SHORT);
            toast.getView().setBackgroundResource(R.drawable.toast_red);
            toast.show();
        }
    }

}