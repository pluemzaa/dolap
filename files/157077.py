<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab 1- 683380344-3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:42:13 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MTI6MTQgUE07MjU3Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDI6MTMgUE07NDsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, rate" type="Real" array="False" size=""/>
            <declare name="year, i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="n" expression="1"/>
            <assign variable="rate" expression="i / 100"/>
            <while expression="n &lt;= year">
                <assign variable="money" expression="money + (money * rate)"/>
                <output expression="&quot;Year &quot;&amp;n&amp;&quot;:&quot;&amp;money" newline="True"/>
                <assign variable="n" expression="n + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>