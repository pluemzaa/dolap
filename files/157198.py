<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="bank"/>
        <attribute name="authors" value="Theerapong-PC01"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:59:26 PM"/>
        <attribute name="created" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjUwOjAyIFBNOzM2NzQ="/>
        <attribute name="edited" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjU5OjI2IFBNOzE7Mzc5Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i" type="Integer" array="False" size=""/>
            <declare name="money, interest, year" type="Real" array="False" size=""/>
            <output expression="&quot;input money (%):&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="i" expression="i+1"/>
                <assign variable="money" expression="money*(1+(interest*0.01))"/>
                <output expression="&quot;Year&quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>