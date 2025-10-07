<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:59:18 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6Mzc6MzQgUE07MjU4Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTk6MTggUE07MzsyNjk4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <declare name="money, interest, sum" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i &lt; years">
                <assign variable="sum" expression="money * (1 + interest/100)"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot; &amp;sum" newline="True"/>
                <assign variable="money" expression="sum"/>
            </while>
        </body>
    </function>
</flowgorithm>