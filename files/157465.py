<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 03:58:35 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xOTswMzoyOToxMyBQTTsyNzI2"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xOTswMzo1ODozNSBQTTs1OzI4NDQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i&lt;year">
                <assign variable="money" expression="money * (1+interest/100)"/>
                <output expression="&quot;year &quot;&amp;(i+1)&amp;&quot;:&quot;&amp;(money)" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>