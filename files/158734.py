<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab3"/>
        <attribute name="authors" value="ACER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 11:07:13 PM"/>
        <attribute name="created" value="QUNFUjtBQ0VSX1A7MjU2OC0wNy0xNjswODowODowNSBQTTsyMDQx"/>
        <attribute name="edited" value="QUNFUjtBQ0VSX1A7MjU2OC0wNy0yMjsxMTowNzoxMyBQTTs1OzIxNDI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, rate, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="rate"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="1"/>
            <while expression="i &lt;= years">
                <assign variable="money" expression="money * (1 + rate / 100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>