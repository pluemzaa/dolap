<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="dd"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 11:18:00 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMDoyODo0NyBQTTsyNjcx"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMToxODowMCBQTTsyOzI3Njk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; years">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;year &quot;&amp;(i+1)&amp; &quot;:&quot; &amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>