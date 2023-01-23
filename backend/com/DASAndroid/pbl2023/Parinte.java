package com.DASAndroid.pbl2023;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Parinte {
    public static JSONObject createNewChildJson(String name_surname_copil, String name_surname_parinte) throws IOException, JSONException {
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("name_surname_copil", name_surname_copil);
        sender_jo.put("name_surname_parinte", name_surname_parinte);
        return sender_jo;
    }

    public static void postNewChildAdd(JSONObject login_jo ) throws IOException {
        String url = "http://127.0.0.1:5000/addchildsparinte";
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json");
        String json = login_jo.toString();
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
        System.out.println(response.toString());
    }
}
