<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="mathtest"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 07:55:23 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTc6MjkgUE07MjU4Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDY6MDcgUE07MjsyNjg2"/>
        <attribute name="edited" value="YWNlcjtMQVBUT1AtNk9PQzRDTFM7MjAyNS0wNy0yMTswNzo1NToyMyBQTTszOzI4NzI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Realmoney, inter, year, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="Realmoney"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="inter"/>
            <assign variable="inter" expression="inter/100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="i" expression="i+1"/>
                <assign variable="Realmoney" expression="Realmoney*(1+inter)"/>
                <output expression="&quot;Year&quot;&amp; i &amp;&quot; :&quot;&amp;Realmoney" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>