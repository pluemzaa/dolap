<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3607;&#3657;&#3634;&#3618;"/>
        <attribute name="authors" value="WINDOWS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 07:00:31 PM"/>
        <attribute name="created" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMjswNjo0OToxNyBQTTsyOTM4"/>
        <attribute name="edited" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMjswNzowMDozMSBQTTszOzMwMzI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, vat, total, sum" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="vat"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i&lt;year">
                <assign variable="money" expression="money*(1+(vat/100))"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;:&quot;&amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>