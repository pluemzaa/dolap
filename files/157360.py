<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="money"/>
        <attribute name="authors" value="ITSeed"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 06:55:02 PM"/>
        <attribute name="created" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjQ5OjIzIFBNOzI4ODE="/>
        <attribute name="edited" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjU1OjAyIFBNOzE7Mjk4Mw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <declare name="money, interest, sum" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;years">
                <assign variable="sum" expression="money*(1+interest/100)"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;:&quot;&amp;sum" newline="True"/>
                <assign variable="money" expression="sum"/>
            </while>
        </body>
    </function>
</flowgorithm>