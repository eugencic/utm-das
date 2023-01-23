package com.DASAndroid.pbl2023;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Users {
    public static JSONObject createUserJson(String username, String password ) throws IOException, JSONException {
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("username", username);
        sender_jo.put("password", password);
        return sender_jo;
    }

    public static JSONObject createNewElevJson(String username, String password, String idnp, String name_surname, String clasa, String liceu, String parinte ) throws IOException, JSONException {
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("username", username);
        sender_jo.put("password", password);
        sender_jo.put("idnp", idnp);
        sender_jo.put("name_surname", name_surname);
        sender_jo.put("clasa", clasa);
        sender_jo.put("liceu", liceu);
        sender_jo.put("parinte", parinte);
        return sender_jo;
    }

    public static JSONObject createNewProfJson(String username, String password, String name_surname, String obiect ) throws IOException, JSONException {
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("username", username);
        sender_jo.put("password", password);
        sender_jo.put("name_surname", name_surname);
        sender_jo.put("obiect", obiect);
        return sender_jo;
    }

    public static JSONObject createNewParinteJson(String username, String password, String idnp, String name_surname, String liceu, String posta ) throws IOException, JSONException {
        JSONObject sender_jo = new JSONObject();
        sender_jo.put("username", username);
        sender_jo.put("password", password);
        sender_jo.put("idnp", idnp);
        sender_jo.put("name_surname", name_surname);
        sender_jo.put("liceu", liceu);
        sender_jo.put("posta", posta);
        return sender_jo;
    }

    public static void postUserLoghInMessage(JSONObject login_jo ) throws IOException {
        String url = "http://127.0.0.1:5000/login";
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

    public static void postCreateNewElev(JSONObject jo ) throws IOException {
        String url = "http://127.0.0.1:5000/signupelev";
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
        System.out.println(response.toString());
    }

    public static void postCreateNewParinte(JSONObject jo ) throws IOException {
        String url = "http://127.0.0.1:5000/signupparinte";
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
        System.out.println(response.toString());
    }

    public static void postCreateNewProfesor(JSONObject jo ) throws IOException {
        String url = "http://127.0.0.1:5000/signupprof";
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
        System.out.println(response.toString());
    }
}
