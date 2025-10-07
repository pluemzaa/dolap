<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4.4"/>
        <attribute name="authors" value="asus"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 09:32:35 PM"/>
        <attribute name="created" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswOTowMjowMSBQTTsyNzU3"/>
        <attribute name="edited" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswOTozMjozNSBQTTszOzI4Nzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, x, years, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="x"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;years">
                <assign variable="i" expression="i+1"/>
                <assign variable="money" expression="money*(1+(x/100))"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>