/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package scraping;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

/**
 *
 * @author aiyerganapathy
 */
public class Scraping {

    /**
     * @param args the command line arguments
     */
    static String movie_name="",country="",year;
    static int flag=0;
    public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException, IOException {
        String fileName = "C:\\Users\\Aiyer\\Desktop\\blah\\thriller.html";
        PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Users\\Aiyer\\Desktop\\names2.txt", true)));
    
        //String line = null;

        try {
            Scanner input = new Scanner(new File(fileName));
            int td_count=0;
            while(input.hasNextLine())
            {
                String data = input.nextLine();
                if(data.contains("in film\">")){
                    year=data.substring(data.indexOf("in film\">")+9);
                    year=year.substring(0,year.indexOf("</"));
                    System.out.println(year);
                }else{
                if(data.contains("<td><i>")){
                    
                    movie_name=data.substring(data.indexOf("\">")+2);
                    td_count=1;
                    if(!movie_name.contains("td><i><b>")){
                       flag=1;
                    movie_name=movie_name.substring(0, movie_name.indexOf("</a>"));
                    //System.out.println(movie_name);
                    }
                }
                else{
                    if(data.contains("<td>")){
                        td_count++;
                        if(td_count==4){
                            if(!data.contains("<td></td>")){
                            country=data.substring(data.indexOf("title=\"")+7);
                            country=country.substring(0,country.indexOf("\">"));
                            if(country.equals("United States")){
                               // System.out.println(movie_name);
                                if(flag==1){
                                    writer.println(movie_name+","+year);
                                    flag=0;
                                }
                            }
                            }
                        }
                    }
                }
            }  
            }
        writer.close();
        }
        catch (IOException e){
            System.out.println(e);
        }
    }
    
}
