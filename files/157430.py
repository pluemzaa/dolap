<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="f3"/>
        <attribute name="authors" value="thasa"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 03:16:47 AM"/>
        <attribute name="created" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTk7MDM6MTA6MjUgQU07Mjg0MQ=="/>
        <attribute name="edited" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTk7MDM6MTY6NDcgQU07MjsyOTYw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, year, x, y" type="Real" array="False" size=""/>
            <assign variable="y" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="x"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <while expression="y&lt;year">
                <assign variable="y" expression="y+1"/>
                <assign variable="money" expression="money*(1+(x/100))"/>
                <output expression="&quot;Year&quot;&amp;y&amp;&quot;:&quot;&amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>